import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import BookList from './components/Books.js';
import AuthorBookList from './components/AuthorBooks.js';
import axios from 'axios';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

const NotFound404 = ({ location}) => {
   return (
   <div>
        <h1>Страница по адресу `{location.pathname}` не найдена</h1>
   </div>
    )
}

class App extends React.Component {
    constructor(props) {
      super(props)
      const author1 = {id: 1, first_name: 'Грин', birthday_year: 1800}
      const author2 = {id: 2, first_name: 'Пушкин', birthday_year: 1799}
      const authors = [author1, author2]

      const book1 = {id: 1, name: 'Алые паруса', author: author1}
      const book2 = {id: 2, name: 'Золотая цепь', author: author1}
      const book3 = {id: 3, name: 'Пиковая дама', author: author2}
      const book4 = {id: 4, name: 'Капитанская дочка', author: author2}
      const books = [book1, book2, book3, book4]

      this.state = {
                'authors': authors,
                'books': books
      }
  }
   /* componentDidMount() {
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
   */

    //componentDidMount() {
      //  const authors = [
       //     {
         //       'first_name': 'Фёдор',
           //     'last_name': 'Достоевский',
             //   'birthday_year': 1821
           // },
           // {
             //   'first_name': 'Александр',
              //  'last_name': 'Грин',
               // 'birthday_year': 1880
           // },
       // ]
        //this.setState(
        //    {
          //      'authors': authors
          //  }
       // )
   // }
  
    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' component={() => <BookList items={this.state.books} />} />
                        <Route exact path='/author/:id' component={() => <AuthorBookList items={this.state.books} />} />
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;