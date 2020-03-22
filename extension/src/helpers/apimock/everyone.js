import { mockasync } from './mockutils'
import { todoList } from './db_todo'

export default {
  getTodos() {
    return mockasync(todoList).then(response => response.data)
  },
  addNewTodo(newTodo) {
    if (newTodo.text === 'kaboom') {
      return mockasync({ error: 'addNewTodo() goes boom!' }).then(
        response => response.data
      )
    }
    newTodo.id = Math.random() * 10
    return mockasync(newTodo).then(response => response.data)
  },
  removeTodo(todo) {
    return mockasync(todo).then(response => response.data)
  }
}