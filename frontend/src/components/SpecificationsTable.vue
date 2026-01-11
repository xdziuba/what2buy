<template>
  <q-table
    dense
    flat
    hide-header
    :rows="rows"
    :columns="columns"
    row-key="name"
  />
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  specs: {
    type: Array,
    required: true
  }
})

const columns = [
  {
    name: 'name',
    label: 'Parametr',
    field: 'name',
    align: 'left'
  },
  {
    name: 'value',
    label: 'Wartość',
    field: 'value',
    align: 'left'
  }
]

const rows = computed(() => props.specs)
</script>
