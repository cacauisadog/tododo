<template>
  <div>
    <h1 class="ml-2">
      tododo
    </h1>
    <div class="mt-2">
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-3 rounded-full ml-2"
        @click="newTodoList()"
      >
        <p>New todo list</p>
      </button>
      <div
        v-if="todoLists && todoLists.length > 0"
        class="flex flex-wrap"
      >
        <TodoList
          v-for="todoList in todoLists"
          :key="todoList.id"
          :todo-list="todoList"
          @save-tododo="saveTododo"
          @save-list-title="saveListTitle"
          @remove-todo-list="removeTodoList"
          @add-new-todo="addNewTodo"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { generateRandomCode } from '@/helpers/math.js'
import TodoList from '@/components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoList
  },
  data () {
    return {
      tododo: undefined,
      todoLists: undefined
    }
  },
  created () {
    const tododo = JSON.parse(localStorage.getItem('tododo') || '{"todoLists": []}')
    this.tododo = tododo
    this.todoLists = tododo.todoLists
  },
  methods: {
    newTodoList () {
      this.todoLists.push(
        {
          id: generateRandomCode(),
          title: 'New list',
          todos: []
        }
      )
      this.saveTododo()
    },
    removeTodoList (todoList) {
      const index = this.todoLists.indexOf(todoList)
      this.todoLists.splice(index, 1)
      this.saveTododo()
    },
    saveListTitle (todoList) {
      let list = this.todoLists.find(t => t.id === todoList.id)
      list.title = todoList.title
      this.saveTododo()
    },
    addNewTodo (todoList) {
      let list = this.todoLists.find(t => t.id === todoList.id)
      list.todos.push(todoList.newTodo)
      this.saveTododo()
    },
    saveTododo () {
      localStorage.setItem('tododo', JSON.stringify(this.tododo))
    }
  }
}
</script>
