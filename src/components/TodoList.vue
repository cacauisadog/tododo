<template>
  <div class="card pa-3 ma-2">
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
        @remove-todo="removeTodo"
        @save-text="saveText"
        @save-isdone="saveIsDone"
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

<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  height: 450px;
  width: 450px;
  background-color: rgb(242, 248, 222);
  box-shadow: inset 0 -3em 3em rgba(0, 0, 0, 0.1),
    0.3em 0.3em 1em rgba(0, 0, 0, 0.3);
}

.todos {
  max-height: 270px;
  overflow-y: auto;
}
</style>