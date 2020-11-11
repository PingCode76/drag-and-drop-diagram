console.log(Vue)

const app = new Vue({
    el: '#app',
    data: {
        diagramTitle: 'Title of function',
        txtLabel: 'Mon texte',
    },
    delimiters: ['[[', ']]'] // Use this in a template // useful not to confuse with the {{ }} syntax of flask
})

console.log("main.js executed");