<template>
<q-page class="q-pa-md">
    <div v-if="!result">Brak wyników</div>

    <div v-else class="row justify-center q-col-gutter-md">
      <div
        v-for="marketplace in result.marketplaces"
        :key="marketplace.marketplace"
        class="col-12 col-md-4"
      >
        <MarketplaceColumn :marketplace="marketplace" />
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useSearchStore } from 'src/stores/search'
import MarketplaceColumn from 'components/MarketplaceColumn.vue'

const searchStore = useSearchStore()
const { result } = storeToRefs(searchStore)
</script>
