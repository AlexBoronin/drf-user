import React from 'react'

const BookItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {author.item.lastname}
            </td>
        </tr>
    )
}

const BookList = ({items}) => {
    return (
        <table border="1" cellspacing="0" cellpadding="0" bgcolor="#00ced1">
            <th>
                ID
            </th>
            <th>
                Name
            </th>
            <th>
                Author
            </th>
            {items.map((item) => <BookItem item={item} />)}
        </table>
    )
}

export default BookList
