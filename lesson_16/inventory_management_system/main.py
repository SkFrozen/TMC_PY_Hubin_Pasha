from flask import Flask, jsonify, redirect, render_template, request
from models.base import Base, engine, engine2
from models.categories import Category
from models.goods import Good
from models.orders import Order
from models.providers import Provider
from sqlalchemy.orm import sessionmaker
from views.goods import add_good, delete_good, get_info_good

metadata = Base.metadata

app = Flask(__name__)
session_pool = sessionmaker(bind=engine)


@app.route("/home")
def home():
    return render_template("/index.html", route="home")


@app.route("/errors")
def errors():
    return render_template("/errors.html")


@app.route("/providers")
def get_providers():
    with session_pool() as session:
        providers = session.query(Provider).all()
    return render_template("providers.html", providers=providers, route="providers")


@app.route("/goods", methods=["GET", "POST"])
def get_goods():
    if request.method == "POST":
        with session_pool() as session:
            good = get_info_good(session, request.json.get("id"))
            provider = (
                session.query(Provider).filter(Provider.id == good.provider_num).first()
            )
            category = (
                session.query(Category).filter(Category.id == good.category_num).first()
            )
            json = jsonify(
                {
                    "id": good.id,
                    "name": good.name,
                    "cost": good.cost,
                    "provider": provider.company_name,
                    "category": category.name,
                }
            )
            return json
    with session_pool() as session:
        goods = (
            session.query(Good, Provider.company_name, Category.name)
            .filter(Good.provider_num == Provider.id)
            .filter(Good.category_num == Category.id)
            .all()
        )
        providers = session.query(Provider.company_name).all()
        categories = session.query(Category.name).all()
    return render_template(
        "goods.html",
        goods=goods,
        route="goods",
        providers=providers,
        categories=categories,
    )


@app.route("/goods/add", methods=["POST"])
def add_goods():
    if request.method == "POST":
        try:
            with session_pool() as session:
                add_good(
                    session,
                    name=request.form["name"],
                    cost=request.form["cost"],
                    provider=request.form["provider"],
                    category=request.form["category"],
                )
                session.commit()
        except Exception as e:
            return render_template("errors.html", e=e)
    return redirect("/goods")


@app.route("/goods/update", methods=["POST"])
def update_goods():
    if request.method == "POST":
        with session_pool() as session:
            print(request.form["good_id"])
            provider = (
                session.query(Provider)
                .filter_by(company_name=request.form["provider"])
                .first()
            )
            category = (
                session.query(Category).filter_by(name=request.form["category"]).first()
            )
            session.query(Good).filter_by(id=request.form["good_id"]).update(
                {
                    "name": request.form["name"],
                    "cost": request.form["cost"],
                    "provider_num": provider.id,
                    "category_num": category.id,
                }
            )
            session.commit()
            return redirect("/goods")


@app.route("/goods/delete/<id_g>", methods=["GET"])
def delete_goods(id_g):
    with session_pool() as session:
        try:
            delete_good(session, id_g)
            session.commit()
        except Exception as e:
            return redirect("/orders")
    return redirect("/goods")


@app.route("/orders", methods=["GET", "POST"])
def get_orders():
    with session_pool() as session:
        orders = session.query(Order, Good.name).filter(Order.good_num == Good.id).all()
    return render_template("orders.html", orders=orders, route="orders")


if __name__ == "__main__":
    # metadata.create_all(engine)
    app.run("localhost", 5000)
    pass
