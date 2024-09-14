const popupOverlay = document.getElementById("popup-overlay");
const popup = document.getElementById("popup")
const popup_good = document.getElementById("popup_good")

document.querySelectorAll(".btn_good").forEach(el =>
	el.addEventListener('click', async () => {
		let obj = { 'id': el.value }
		let response = await fetch('/goods', {
			method: "POST",
			headers: {
				"Content-Type": "application/json;charset=utf-8"
			},
			body: JSON.stringify(obj)
		});
		let result = await response.json();
		let name = document.getElementById("popup_name")
		let cost = document.getElementById("popup_cost")
		let provider = document.getElementById("popup_provider")
		let category = document.getElementById("popup_category")
		let id = document.getElementById("popup_id")
		name.value = result.name
		cost.value = result.cost
		id.setAttribute("value", result.id)
		if (provider.querySelector(`option[value='${result.provider}']`)) {
			provider.value = result.provider
		}
		if (category.querySelector(`option[value='${result.category}']`)) {
			category.value = result.category
		}
	})
);

document.querySelectorAll(".btn_provider").forEach(el =>
	el.addEventListener('click', async () => {
		let obj = { 'id': el.value }
		let response = await fetch('/providers', {
			method: "POST",
			headers: {
				"Content-Type": "application/json;charset=utf-8"
			},
			body: JSON.stringify(obj)
		});
		let result = await response.json();
		let first_name = document.getElementById("popup_first_name")
		let last_name = document.getElementById("popup_last_name")
		let email = document.getElementById("popup_email")
		let company_name = document.getElementById("popup_company_name")
		let id = document.getElementById("popup_id")
		first_name.value = result.first_name
		last_name.value = result.last_name
		email.value = result.email
		company_name.value = result.company_name
		id.setAttribute("value", result.id)
	})
);

document.querySelectorAll(".btn_order").forEach(el =>
	el.addEventListener('click', async () => {
		let obj = { 'id': el.value }
		let response = await fetch('/orders', {
			method: "POST",
			headers: {
				"Content-Type": "application/json;charset=utf-8"
			},
			body: JSON.stringify(obj)
		});
		let result = await response.json();
		let name = document.getElementById("popup_name")
		let address = document.getElementById("popup_address")
		let notes = document.getElementById("popup_notes")
		let email = document.getElementById("popup_email")
		let status = document.getElementById("popup_status")
		let good = document.getElementById("popup_good")
		let id = document.getElementById("popup_id")
		name.value = result.name
		address.value = result.address
		notes.value = result.notes
		email.value = result.email
		status.value = result.status
		if (good.querySelector(`option[value='${result.good_id}']`)) {
			good.querySelector(`option[value='${result.good_id}']`).setAttribute("selected", "selected")
		}
		id.setAttribute("value", result.id)
	})
);

function showPopup() {
	popupOverlay.style.display = "block";
}

function hidePopup() {
	if (popup_good) {
		popup_good.querySelector("option[selected=selected]").removeAttribute("selected")
	};
	popupOverlay.style.display = "none";
}


popupOverlay.addEventListener("click", hidePopup);
popup.addEventListener("click", (event) => { event.stopPropagation() });
