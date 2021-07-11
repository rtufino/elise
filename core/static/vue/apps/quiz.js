var mess = '';
            var tit = '';
            var typ = '';
            var quizApp = new Vue({
                el: '#quizApp',
                delimiters: ['[[',']]'],
                data() {
                    return {
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
                        var currentdate = new Date()
                        var data = {
                            'name': this.name,
                            'state': this.state === '' ? 0 : 1,
                            'vig_date': this.vig_date,
                            'type': this.type + 'hola',
                            'start_date': currentdate.getFullYear() + '-' + currentdate.getMonth() + '-' + currentdate.getDate(),
                        }
                        console.log(data);
                        fetch('/psicologo/api/addQuiz', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': '{{ csrf_token }}'
                            },
                            credentials: 'same-origin',
                            body: JSON.stringify(data)
                        })
                            .then((response) => {
                                console.log('Success')
                                console.log(response)
                                if (response.ok) {
                                    mess = 'Registro Creado!'
                                    typ = 'success'
                                    tit = 'Excelente!'
                                    this.showToast(mess, typ, tit);
                                    this.name = ''
                                    this.vig_date = ''
                                } else {
                                    mess = 'No se ha podido guardar el registro...'
                                    typ = 'error'
                                    tit = 'Oh no!'
                                    this.showToast(mess, typ, tit);
                                }
                            })
                            .catch((error) => {
                                mess = error
                                typ = 'error'
                                tit = 'Error Fatal!'
                                this.showToast(mess, typ, tit);
                            })
                    },
                    showToast(mess, typ, tit) {
                        toastr[typ](mess, tit, {
                            positionClass: 'toast-top-right',
                            timeOut: '2500'
                        });
                    }
                }
            })