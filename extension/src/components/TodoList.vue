<template>
  <div class="card pa-3">
    <h2 class="mb-2">
      <input
        id="todolisttitle"
        ref="titleInput"
        v-model.lazy="title"
        style="width: 100%;"
        type="text"
        name="title"
      >
    </h2>
    <div v-if="todos && todos.length > 0">
      <todo-item
        v-for="todo in todos"
        :key="todo.id"
        :item="todo"
        @removeTodo="removeTodo($event)"
      />
    </div>
    <p v-else>
      please add a todo
    </p>
    <p v-if="loadingTodo">
      todo action loading!
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
    todoList: {
      type: Object,
      required: true,
      default: () => { },
      validator: value => {
        return (
          typeof value['id'] === 'number' &&
          typeof value['title'] === 'string' &&
          Array.isArray(value.todos)
        )
      }
    }
  },
  data () {
    return {
      newTodoText: '',
      loadingTodo: false
    }
  },
  computed: {
    title: {
      get () {
        return this.todoList.title
      },
      set (value) {
        if (!value) {
          value = 'New todo list'
        } else {
          this.editTodoListTitle()
          this.$refs.titleInput.blur()
        }
      }
    },
    todos () {
      return this.todoList.todos
    }
  },
  methods: {
    editTodoListTitle () {
      api.everyone.editTodoListTitle(this.todoList.id, this.todoList.title).then(response => {
        if (response.error) {
          console.log('error saving todo list title', response.error)
        }
      })
    },
    addNewTodo () {
      if (this.newTodoText === '') return
      this.loadingTodo = true
      const newTodo = {
        todoListId: this.todoList.id,
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
  height: 400px;
  width: 300px;
  background-color: rgb(242, 248, 222);
  box-shadow: inset 0 -3em 3em rgba(0, 0, 0, 0.1),
    0.3em 0.3em 1em rgba(0, 0, 0, 0.3);
}
</style>