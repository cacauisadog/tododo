<template>
  <div>
    <h1>tododo</h1>
    <div class="mt-4">
      <button
        class="button"
        @click="newTodoList()"
      >
        <p>New todo list</p>
      </button>
      <div
        v-if="todoLists && todoLists.length > 0"
        class="todolists ma-2"
      >
        <TodoList
          v-for="todoList in todoLists"
          :key="todoList.id"
          :todo-list="todoList"
          @save-tododo="saveTododo()"
          @remove-todo-list="removeTodoList($event)"
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
    saveTododo () {
      localStorage.setItem('tododo', JSON.stringify(this.tododo))
    }
  }
}
</script>

<style lang="scss">
@import "@/assets/css/main.scss";

.todolists {
  display: flex;
  flex-wrap: wrap;
}
</style>
