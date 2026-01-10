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

<script setup lang="ts">
import { computed } from 'vue'
import type { QTableColumn } from 'quasar'
import type { Specification } from 'src/types/SearchResult'

const props = defineProps<{
  specs: Specification[]
}>()

const columns: QTableColumn[] = [
  { name: 'name', label: 'Parametr', field: 'name', align: 'left' },
  { name: 'value', label: 'Wartość', field: 'value', align: 'left' }
]

const rows = computed(() => props.specs)
</script>
