import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import BookList from './components/Books.js'
import axios from 'axios'
import WebtodoserviceList from "./components/webtodoservice.js"
import {HashRouter, Route, Switch, Redirect} from 'react-router-dom'
import AuthorBookList from "./components/AuthorBook";
import LoginForm from "./components/Auth";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>)
}

class App extends React.Component {
    constructor(props) {
        super(props)


        this.state = {
            'authors': authors,
            'books': books,
            'token': '',
        }
    }

    set_token(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    logout (){
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated(){
    return this.state.token !== ''
    }

    get_token(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: login, password: password})
            .then(response => {
                this.setState(response.data['token'])
            }).catch(error => alert('Неверный пароль'))
    }

    get_headers () {
        let headers = {
            'Content-Type': 'application/json',
        }
        if (this.is_authenticated()){
            headers['Authorization'] = 'Token' + this.state.token
        }
        return headers
    }

     load_data()  {
     const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors', {headers})
            .then(response => {
                const authors = response.data
                    this.setState(
                    {
                        'authors': authors['results']
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/books', {headers})
            .then(response => {
                const books = response.data['results']
                    this.setState(
                    {
                        'books': books
                    }
                )
            }).catch(error => console.log(error))
    }

    componentDidMount(){
        this.get_token_from_storage()
    }

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
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout}>logout</button>
                                : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList items={this.state.books}/>}/>
                        <Route exact path='/author/:id' component={() => <AuthorBookList items={this.state.books}/>}/>
                        <Route exact path='/login' component={() => <LoginForm get_token{(login, password) =>
                        this.get_token(login, password)}/>}/>
                        <Redirect from='authors' to='/'></Redirect>
                        <Route component={NotFound404}></Route>
                    </Switch>
                </HashRouter>
            </div>
        )
    }
}

export default App;