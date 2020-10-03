<template>
  <div class="flex align-center">
    <input
      v-model="isDone"
      class="isDoneCheckbox"
      type="checkbox"
    >
    <input
      id="todotext"
      ref="textInput"
      v-model.lazy="todoText"
      style="width: 100%; outline: none;"
      type="text"
      name="todotext"
      :class="{ 'text-linethrough': item.isDone }"
      class="todo-text fs-m mb-1"
      :readonly="textDisabled"
      @click="item.isDone = !item.isDone"
      @dblclick="textDisabled = false"
    >
    <button
      class="ml-2"
      @click="$emit('remove-todo', item)"
    >
      [X]
    </button>
  </div>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    item: {
      type: Object,
      required: true,
      validator: value => {
        return (
          !!value['id'].match(/^[a-zA-Z0-9]*$/) &&
          typeof value['text'] === 'string' &&
          typeof value['isDone'] === 'boolean'
        )
      }
    }
  },
  data () {
    return {
      textDisabled: true
    }
  },
  computed: {
    todoText: {
      get () {
        return this.item.text
      },
      set (value) {
        this.item.text = value
        this.$emit('save-tododo')
        this.$refs.textInput.blur()
      }
    },
    isDone: {
      get () {
        return this.item.isDone
      },
      set (value) {
        this.item.isDone = value
        this.$emit('save-tododo')
      }
    }
  }
}
</script>

<style>
.flex {
  display: flex;
  align-items: center;
}

.isDoneCheckbox {
  margin-left: 8px;
  margin-top: 2px;
  margin-right: 2px;
}

.text-linethrough {
  text-decoration: line-through;
}

.todo-text {
  font-family: "Comic Neue", cursive;
  font-weight: 300;
}
</style>
