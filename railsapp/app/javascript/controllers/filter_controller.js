import { Controller } from "@hotwired/stimulus"
export default class extends Controller {
  static targets = ["riscoDeChurn", "cardStatus", "name", "list"]
  connect() {
    console.log("Filter controller connected");
  }
  filter() {
    const url = `/?` +
                `risco_de_churn=${this.riscoDeChurnTarget.value}&` +
                `card_status=${this.cardStatusTarget.value}&` +
                `name=${this.nameTarget.value}`;
    fetch(url, { headers: { 'Accept': 'text/plain' } })
      .then(response => response.text())
      .then(html => {
        // console.log(html);
        this.listTarget.innerHTML = html
      });
  }
}
