Vue.component('message', {
    template: `
    <div id="toast-container" class="toast-top-right">
        <div class="toast toast-success" aria-live="polite" style="">
        <div class="toast-progress" style="width: 64.4%;"></div>
        <button type="button" class="toast-close-button" role="button">×</button>
        <div class="toast-message">My name is Inigo Montoya. You killed my father. Prepare to die!</div>
        </div>
    </div>
    `
})