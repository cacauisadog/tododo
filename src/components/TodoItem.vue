<template>
  <div class="flex">
    <input
      v-model="isDone"
      class="isDoneCheckbox mr-1 h-5 w-5"
      type="checkbox"
    >
    <p
      :class="{
        'line-through': item.isDone,
        'text-gray-500': item.isDone
      }"
      class="text-base mb-3 overflow-auto resize-none w-full break-all"
    >
      {{ item.text }}
    </p>
    <button
      class="ml-2 h-5 w-5 text-red-600"
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
  computed: {
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
