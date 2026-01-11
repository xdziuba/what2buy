<template>
  <q-expansion-item
    expand-separator
    icon="shopping_cart"
    :label="product.name"
  >
    <q-card flat>
      <q-card-section>
        <div><strong>Cena:</strong> {{ product.price }} zł</div>
        <div><strong>Ocena:</strong> {{ product.rating }}</div>
        <div>
          <a :href="product.url" target="_blank" rel="noopener noreferrer">
            Przejdź do oferty
          </a>
        </div>
      </q-card-section>

      <q-separator />

      <q-card-section>
        <SpecificationsTable :specs="product.specifications" />
      </q-card-section>
    </q-card>
  </q-expansion-item>
</template>

<script setup>
import SpecificationsTable from './SpecificationsTable.vue'

defineProps({
  product: {
    type: Object,
    required: true
  }
})
</script>
