<template>
  <q-table
    dense
    flat
    dark
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
            <a
              :href="productUrl(props.col.name)"
              target="_blank"
              rel="noopener noreferrer"
              class="product-link"
              @click.stop
            >
              {{ props.col.label }}
            </a>
          </div>
          <div class="text-caption text-grey-5">
            {{ productPrice(props.col.name) }} zł
          </div>
        </div>
        <span v-else>
          Specification
        </span>
      </q-th>
    </template>

    <template #body-cell="props">
      <q-td
        :props="props"
        :class="props.row._different && props.col.name !== 'spec'
          ? 'diff-cell'
          : ''"
      >
        {{ props.value }}
      </q-td>
    </template>
  </q-table>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  products: {
    type: Array,
    required: true
  }
})

const productMap = computed(() => {
  return Object.fromEntries(
    props.products.map(p => [p.name, p])
  )
})

const columns = computed(() => {
  if (!props.products.length) return []

  return [
    {
      name: 'spec',
      label: 'Specification',
      field: 'spec',
      align: 'left'
    },
    ...props.products.map(product => ({
      name: product.name,
      label: product.name,
      field: product.name,
      align: 'center'
    }))
  ]
})

const rows = computed(() => {
  if (!props.products.length) return []

  const specs = props.products[0].specifications

  return specs.map(spec => {
    const row = { spec: spec.name }

    const values = []

    props.products.forEach(product => {
      const found = product.specifications.find(
        s => s.name === spec.name
      )
      const value = found ? found.value : '—'
      row[product.name] = value
      values.push(value)
    })

    const unique = new Set(values)
    row._different = unique.size > 1

    return row
  })
})

function productPrice(productName) {
  const product = productMap.value[productName]
  return product ? product.price.toFixed(2) : ''
}

function productUrl(productName) {
  const product = productMap.value[productName]
  return product ? product.url : '#'
}
</script>

<style scoped>
.q-table td,
.q-table th {
  white-space: normal;
}

.product-link {
  color: inherit;
  text-decoration: underline;
  pointer-events: auto;
}

.product-link:hover {
  text-decoration: underline;
}

.diff-cell {
  background: rgba(255, 193, 7, 0.25);
  font-weight: 600;
}
</style>
