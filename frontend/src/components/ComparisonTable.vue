<template>
  <q-table
    dense
    flat
    bordered
    :rows="rows"
    :columns="columns"
    row-key="spec"
    hide-bottom
  >

    <template #header-cell="props">
      <q-th :props="props">
        <div v-if="props.col.name !== 'spec'" class="column items-center">
          <div class="text-weight-medium">
            {{ props.col.label }}
          </div>
          <div class="text-caption text-grey-5">
            {{ productPrice(props.col.name) }} zł
          </div>
        </div>
        <span v-else>
          Specyfikacja
        </span>
      </q-th>
    </template>
  </q-table>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { QTableColumn } from 'quasar'
import type { ProductInfo } from 'src/types/SearchResult'


const props = defineProps<{
  products: ProductInfo[]
}>()


const productMap = computed(() =>
  Object.fromEntries(
    props.products.map(p => [p.name, p])
  )
)


const columns = computed<QTableColumn[]>(() => {
  if (!props.products.length) return []

  return [
    {
      name: 'spec',
      label: 'Specyfikacja',
      field: 'spec',
      align: 'left' as const
    },
    ...props.products.map(product => ({
      name: product.name,
      label: product.name,
      field: product.name,
      align: 'center' as const
    }))
  ]
})


const rows = computed(() => {
  if (!props.products.length) return []

  const specs = props.products[0].specifications

  return specs.map(spec => {
    const row: Record<string, string> = {
      spec: spec.name
    }

    props.products.forEach(product => {
      const found = product.specifications.find(s => s.name === spec.name)
      row[product.name] = found?.value ?? '—'
    })

    return row
  })
})


function productPrice(productName: string): string {
  const product = productMap.value[productName]
  return product ? product.price.toFixed(2) : ''
}
</script>

<style scoped>
.q-table td,
.q-table th {
  white-space: normal;
}
</style>
