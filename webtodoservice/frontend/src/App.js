import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data
                    this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <AuthorList authors={this.state.authors} />

                <p>
                    Вся таблица это компонент AuthorList
                    <br/>каждая строчка - это внутренность AuthorList в виде AuthorItem
                    <br/>вся страница html - это App наследуемый от React.Component
                </p>
            </div>
        )
    }
}
export default App;