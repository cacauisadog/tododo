<template>
  <div class="flex align-center">
    <input
      v-model="isDone"
      class="isDoneCheckbox mr-2"
      style="width: 17px; height: 17px;"
      type="checkbox"
    >
    <input
      id="todotext"
      ref="textInput"
      v-model.lazy="todoText"
      style="width: 100%; outline: none;"
      type="text"
      name="todotext"
      :class="{ 'text-linethrough': item.isDone && textDisabled }"
      class="todo-text fs-m mb-1"
      :readonly="textDisabled"
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
        const item = {
          id: this.item.id,
          text: value
        }
        this.$emit('save-text', item)
        this.$refs.textInput.blur()
        this.textDisabled = true
      }
    },
    isDone: {
      get () {
        return this.item.isDone
      },
      set (value) {
        const item = {
          id: this.item.id,
          isDone: value
        }
        this.$emit('save-isdone', item)
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
