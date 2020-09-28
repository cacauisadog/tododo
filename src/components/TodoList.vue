<template>
  <div class="card pa-3">
    <span
      class="fs-xs text-primary clickable"
      @click="$emit('remove-todo-list', todoList)"
    >Delete list</span>
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
    <div
      v-if="todos && todos.length > 0"
      class="todos"
    >
      <TodoItem
        v-for="todo in todos"
        :key="todo.id"
        :item="todo"
        @remove-todo="removeTodo($event)"
        @save-tododo="$emit('save-tododo')"
      />
    </div>
    <p
      v-else
      class="text-inactive"
      style="font-style: italic;"
    >
      please add a todo
    </p>
    <form
      class="flex mt-auto"
      @submit.prevent="addNewTodo()"
    >
      <input
        v-model="newTodoText"
        type="text"
        name="todoText"
        class="input-text pl-1"
      >
      <button
        type="submit"
        class="button button_round ml-1"
      >
        +
      </button>
    </form>
  </div>
</template>

<script>
import { generateRandomCode } from '@/helpers/math.js'
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
          !!value['id'].match(/^[0-9a-z]+$/) &&
          typeof value['title'] === 'string' &&
          Array.isArray(value.todos)
        )
      }
    }
  },
  data () {
    return {
      newTodoText: ''
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
        }
        this.todoList.title = value
        this.$emit('save-tododo')
        this.$refs.titleInput.blur()
      }
    },
    todos () {
      return this.todoList.todos
    }
  },
  methods: {
    addNewTodo () {
      if (this.newTodoText === '') return
      const newTodo = {
        id: generateRandomCode(),
        text: this.newTodoText,
        isDone: false
      }
      this.todoList.todos.push(newTodo)
      this.$emit('save-tododo')
      this.newTodoText = ''
    },
    removeTodo (todo) {
      const index = this.todos.indexOf(todo)
      this.todos.splice(index, 1)
      this.$emit('save-tododo')
    }
  }
}
</script>

<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  height: 400px;
  width: 300px;
  background-color: rgb(242, 248, 222);
  box-shadow: inset 0 -3em 3em rgba(0, 0, 0, 0.1),
    0.3em 0.3em 1em rgba(0, 0, 0, 0.3);
}

.todos {
  max-height: 270px;
  overflow-y: auto;
}
</style>