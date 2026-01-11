<template>
  <q-card flat dark bordered class="q-mb-md">
    <q-card-section class="text-h6 text-center">
      {{ marketplace.marketplace }}
    </q-card-section>

    <q-separator />

    <q-card-section>
      <ComparisonTable :products="marketplace.results" />
    </q-card-section>
  </q-card>
</template>

<script setup>
import ComparisonTable from './ComparisonTable.vue'

defineProps({
  marketplace: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
  .q-card {
    opacity: 0.91;
  }
</style>
