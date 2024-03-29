<template>
  <div class="relative flex flex-col bg-yellow-200 shadow-lg m-4">
    <div class="px-3 pt-3 h-96 w-80">
      <span
        class="text-base text-red-600 cursor-pointer mb-2"
        @click="$emit('remove-todo-list', todoList)"
      >Delete list</span>
      <h2 class="mb-2">
        <input
          id="todolisttitle"
          ref="titleInput"
          v-model.lazy="title"
          type="text"
          name="title"
          class="text-xl w-full font-bold"
        >
      </h2>
      <div
        v-if="todos && todos.length > 0"
        class="hide-scrollbar max-h-72 overflow-y-auto"
      >
        <TodoItem
          v-for="todo in todos"
          :key="todo.id"
          :item="todo"
          @remove-todo="removeTodo"
          @save-text="saveText"
          @save-isdone="saveIsDone"
        />
      </div>
      <p
        v-else
        class="text-gray-500 italic"
      >
        please add a todo
      </p>
    </div>
    <div class="bg-yellow-400 h-12 w-80 px-4 pt-2">
      <form
        class="flex"
        @submit.prevent="addNewTodo()"
      >
        <input
          v-model="newTodoText"
          type="text"
          name="todoText"
          class="w-full border-2 border-solid border-yellow-100 rounded-md text-base"
        >
        <button
          type="submit"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 rounded-full ml-4"
        >
          +
        </button>
      </form>
    </div>
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
          !!value['id'].match(/^[a-zA-Z0-9]*$/) &&
          typeof value['title'] === 'string' &&
          Array.isArray(value['todos'])
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
        const list = {
          id: this.todoList.id,
          title: value
        }
        this.$emit('save-list-title', list)
        this.$refs.titleInput.blur()
      }
    },
    todos () {
      return this.todoList.todos
    }
  },
  methods: {
    saveText (item) {
      let currentItem = this.todos.find(t => t.id === item.id)
      currentItem.text = item.text
      this.$emit('save-tododo')
    },
    saveIsDone (item) {
      let currentItem = this.todos.find(t => t.id === item.id)
      currentItem.isDone = item.isDone
      this.$emit('save-tododo')
    },
    addNewTodo () {
      if (this.newTodoText === '') return
      const newTodo = {
        id: generateRandomCode(),
        text: this.newTodoText,
        isDone: false
      }
      const list = {
        id: this.todoList.id,
        newTodo
      }
      this.$emit('add-new-todo', list)
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

<style scoped>
.hide-scrollbar::-webkit-scrollbar {
   display: none;
 }
</style>