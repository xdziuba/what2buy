<template>
  <q-card flat bordered class="q-mb-md">
    <q-card-section class="text-h6 text-center">
      {{ marketplace.marketplace }}
    </q-card-section>

    <q-separator />

    <q-card-section>
      <ComparisonTable :products="marketplace.results" />
    </q-card-section>
  </q-card>
</template>

<script setup lang="ts">
import ComparisonTable from './ComparisonTable.vue'
import type { MarketplaceProductMatch } from 'src/types/SearchResult'

defineProps<{
  marketplace: MarketplaceProductMatch
}>()
</script>
