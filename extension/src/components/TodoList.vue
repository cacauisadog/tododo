<template>
  <div class="card">
    <h2>{{ title }}</h2>
    <div
      v-if="todos && todos.length > 0"
      class="margin-bottom"
    >
      <todo-item
        v-for="todo in todos"
        :key="todo.id"
        :item="todo"
        @removeTodo="removeTodo($event)"
      />
    </div>
    <p
      v-else
      class="margin-bottom"
    >
      please add a todo
    </p>

    <form @submit.prevent="addNewTodo()">
      <input
        v-model="newTodoText"
        type="text"
        name="todoText"
      >
      <button type="submit">
        +
      </button>
    </form>
    <p v-if="loadingTodo">
      todo action loading!
    </p>
  </div>
</template>

<script>
import api from '~api'
import TodoItem from '@/components/TodoItem.vue'

export default {
  name: 'TodoList',
  components: {
    TodoItem
  },
  props: {
    title: {
      type: String,
      required: true
    },
    todos: {
      type: Array,
      required: false,
      default: () => []
    }
  },
  data () {
    return {
      newTodoText: '',
      loadingTodo: false
    }
  },
  methods: {
    addNewTodo () {
      if (this.newTodoText === '') return
      this.loadingTodo = true
      const newTodo = {
        text: this.newTodoText,
        isDone: false
      }
      api.everyone
        .addNewTodo(newTodo)
        .then(newTodo => {
          if (newTodo.error) {
            console.log(newTodo.error)
          } else {
            this.todos.push(newTodo)
            this.newTodoText = ''
          }
        })
        .finally(() => {
          this.loadingTodo = false
        })
    },
    removeTodo (todo) {
      this.loadingTodo = true
      api.everyone
        .removeTodo(todo.id)
        .then(response => {
          if (response.error) {
            console.log(response.error)
          } else {
            const todoIndex = this.todos.indexOf(todo)
            this.todos.splice(todoIndex, 1)
          }
        })
        .finally(() => {
          this.loadingTodo = false
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.card {
  border: 1px solid black;
  padding: 10px;
}
</style>