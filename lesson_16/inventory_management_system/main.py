from flask import Flask, jsonify, redirect, render_template, request
from models.base import Base, engine, engine2
from models.categories import Category
from models.goods import Good
from models.orders import Order
from models.providers import Provider
from sqlalchemy.orm import sessionmaker

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
            json_data = Good.get_info(id=request.json.get("id"), session=session)
            json = jsonify(json_data)
            return json
    else:
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
                Good.create(
                    name=request.form["name"],
                    cost=request.form["cost"],
                    provider=request.form["provider"],
                    category=request.form["category"],
                    session=session,
                )
                session.commit()
        except Exception as e:
            print(e)
            return render_template("errors.html", e=e)
    return redirect("/goods")


@app.route("/goods/update", methods=["POST"])
def update_goods():
    if request.method == "POST":
        with session_pool() as session:
            good = Good.get_good_by_id(id=request.form.get("good_id"), session=session)
            good.update(
                name=request.form.get("name"),
                cost=request.form.get("cost"),
                provider=request.form.get("provider"),
                category=request.form.get("category"),
                session=session,
            )
            session.commit()
            return redirect("/goods")


@app.route("/goods/delete/<id_g>", methods=["GET"])
def delete_goods(id_g):
    with session_pool() as session:
        try:
            good = Good.get_good_by_id(id=id_g, session=session)
            good.delete(id=id_g, session=session)
            session.commit()
        except Exception as e:
            print(e)
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
