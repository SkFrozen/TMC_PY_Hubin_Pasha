const popupOverlay = document.getElementById("popup-overlay");
const popup = document.getElementById("popup")
const btn_good = document.getElementsByClassName("btn_good")

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
function showPopup() {
	popupOverlay.style.display = "block";
}

function hidePopup() {
	popupOverlay.style.display = "none";
}


popupOverlay.addEventListener("click", hidePopup);
popup.addEventListener("click", (event) => { event.stopPropagation() });
