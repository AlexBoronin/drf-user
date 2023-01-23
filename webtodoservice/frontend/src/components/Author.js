import React from 'react'
import {Link} from 'react-router-dom'

const AuthorItem = ({authors}) => {
    return (
        <tr>
            <td>
                <Link to={'author/${author.id}'}> {author.id}</Link>
            </td>
            <td>
                {author.username}
            </td>
            <td>
                {author.lastname}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table border="1" cellspacing="0" cellpadding="0" bgcolor="#00ced1">
            <th>
                id
            </th>
            <th>
                username
            </th>
            <th>
                lastname
            </th>
            {authors.map((author) => <AuthorItem author={author}/>)}
        </table>
    )
}

export default AuthorList
