console.log(Vue)

const app = new Vue({
    el: '#app',
    data: {
        diagramTitle: 'Title of function',
        costOfApples: 8
    },
    delimiters: ['[[', ']]'] // Use this in a template // useful not to confuse with the {{ }} syntax of flask
})

console.log("main.js executed");