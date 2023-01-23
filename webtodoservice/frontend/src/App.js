import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import BookList from './components/Books.js'
import axios from 'axios'
import WebtodoserviceList from "./components/webtodoservice.js"
import {HashRouter, Route, Switch, Redirect} from 'react-router-dom'
import AuthorBookList from "./components/AuthoBook";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>)
}

class App extends React.Component {
    constructor(props) {
        super(props)
        const author1 = {id: 1, username: 'Грин', lastname: 1880}
        const author2 = {id: 2, username: 'Пушкин', lastname: 1799}
        const author3 = {id: 3, username: 'Чижик', lastname: 2000}
        const authors = {author1, author2, author3}

        const book1 = {id: 1, name: 'Алые паруса', author: author1}
        const book2 = {id: 2, name: 'Мойдодыр', author: author3}
        const book3 = {id: 3, name: 'О царе Салтане', author: 2}
        const book4 = {id: 4, name: 'Шапокляк', author: author3}
        const books = {book1, book2, book3, book4}

        const webtodoservice1 = {id: 1, username: 'Фдуч', lastname: 'Бабайкин'}
        const webtodoservice2 = {id: 2, username: 'Шум', lastname: 'Прыг'}
        const webtodoservice3 = {id: 3, username: 'Шум', lastname: 'Скок'}
        const webtodoservices = {webtodoservice1, webtodoservice2, webtodoservice3}


        this.state = {
            'authors': authors,
            'books': books,
            'webtodoservice': webtodoservices,
        }
    }

//    componentDidMount() {
//        axios.get('http://127.0.0.1:8000/api/authors')
//            .then(response => {
//                const authors = response.data
//                    this.setState(
//                    {
//                        'authors': authors
//                    }
//                )
//            }).catch(error => console.log(error))
//    }

    render() {
        return (
            <div className='App'>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <link to='/'>Authors</>
                            </li>
                            <li>
                                <link to='/books'>Books</>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}/>}/>
                        <Route exact path='/author/:id' component={() => <AuthorBookList books={this.state.books}/>}/>
                        <Redirect from='authors' to='/'></Redirect>
                        <Route component={NotFound404}></Route>
                    </Switch>
                </HashRouter>
            </div>
        )
    }
}

export default App;