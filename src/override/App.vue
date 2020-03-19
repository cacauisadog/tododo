<template>
  <div>
    <h1>tododo</h1>
    <div v-if="todoList.length > 0" class="margin-bottom">
      <todo-item
        v-for="(todo, idx) in todoList"
        :key="idx"
        :item="todo"
        @removeTodo="removeTodo($event)"
      />
    </div>
    <p v-else class="margin-bottom">please add a todo</p>

    <form @submit.prevent>
      <input type="text" name="todoText" v-model="newTodoText" />
      <button type="submit" @click="addNewTodo()">+</button>
    </form>
  </div>
</template>

<script>
import TodoItem from '@/components/TodoItem.vue'

export default {
  name: 'App',
  components: { TodoItem },
  data() {
    return {
      todoList: [
        {
          id: 1,
          text: 'walk the dog',
          isDone: true
        },
        {
          id: 2,
          text: 'go to the market',
          isDone: true
        },
        {
          id: 3,
          text: 'study vuejs',
          isDone: true
        },
        {
          id: 4,
          text: 'read a book',
          isDone: false
        }
      ],
      newTodoText: ''
    }
  },
  methods: {
    addNewTodo() {
      if (this.newTodoText === '') return

      const newTodo = {
        text: this.newTodoText,
        isDone: false
      }
      this.todoList.push(newTodo)
      this.newTodoText = ''
    },
    removeTodo(item) {
      const itemIndex = this.todoList.indexOf(item)
      this.todoList.splice(itemIndex, 1)
    }
  }
}
</script>

<style>
p,
input {
  margin: 0;
}

.margin-bottom {
  margin-bottom: 10px;
}
</style>
