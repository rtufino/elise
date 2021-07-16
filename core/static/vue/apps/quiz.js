var mess = '';
var tit = '';
var typ = '';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
var quizApp = new Vue({
    el: '#quizApp',
    delimiters: ['[[', ']]'],
    data() {
        return {
            id: '',
            name: '',
            state: '',
            vig_date: '',
            type: '',
            start_date: '',
            quiz_list: []
        }
    },
    created() {
        fetch('/psicologo/api/get_encuestas')
            .then(response => response.json())
            .then(data => {
                this.quiz_list = data;
                console.log(this.quiz_list)
            })
    },
    methods: {
        addQuiz() {
            let currentdate = new Date()
            let data = {
                'nombre': this.name,
                'estado': this.state == '' ? 0 : 1,
                'f_vigencia': this.vig_date,
                'tipo': this.type + 'hola',
                'f_inicio': currentdate.getFullYear() + '-' + currentdate.getMonth() + '-' + currentdate.getDate(),
            }
            console.log(data);
            fetch('/psicologo/api/get_encuestas', {
                method: 'POST', // or 'PUT'
                body: JSON.stringify(data), // data can be `string` or {object}!
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                }
            }).then(res => res.json())
                .catch(error => {
                    console.error('Error:', error)
                    mess = error
                    typ = 'error'
                    tit = 'Error Fatal!'
                    this.showToast(mess, typ, tit);
                })
                .then(response => {
                    console.log('Success:', response)
                    if (response.ok) {
                        mess = 'Registro Creado!'
                        typ = 'success'
                        tit = 'Excelente!'
                        this.showToast(mess, typ, tit);
                        this.name = ''
                        this.vig_date = ''
                        this.quiz_list.push(response)
                    } else {
                        mess = 'No se ha podido guardar el registro...'
                        typ = 'error'
                        tit = 'Oh no!'
                        this.showToast(mess, typ, tit);
                    }
                });
        },
        showToast(mess, typ, tit) {
            toastr[typ](mess, tit, {
                positionClass: 'toast-top-right',
                timeOut: '2500'
            });
        },
        cargaQuiz(id) {
            fetch('/psicologo/api/get_encuesta/' + id)
                .then(response => response.json())
                .then(data => {
                    this.id = data.id;
                    this.name = data.nombre;
                    this.state = data.estado;
                    this.vig_date = data.f_vigencia;
                    this.type = data.tipo;
                    this.start_date = data.f_inicio;
                    console.log(this.name);
                    console.log(data);
                })
        },
        updateQuiz() {
            let currentdate = new Date();
            let data = {
                'nombre': this.name,
                'estado': this.state == '' ? 0 : 1,
                'f_vigencia': this.vig_date,
                'tipo': this.type + 'hola',
                'f_inicio': currentdate.getFullYear() + '-' + currentdate.getMonth() + '-' + currentdate.getDate(),
            }
            fetch('/psicologo/api/get_encuesta/' + this.id,{
                method: 'put',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                }
            })
                .then(response => response.json())
                .then(data => {
                    console.log(this.name);
                    console.log(data);
                })
        },
        deleteQuiz() {
            fetch('/psicologo/api/get_encuesta/' + this.id, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                }
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
        }
    }
})