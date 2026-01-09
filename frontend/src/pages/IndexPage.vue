<template>
  <q-page class="flex flex-center">
    <div class="search-content flex column flex-center">
      <div class="text-h2 text-white q-mb-lg">What are we searching today?</div>
      <q-input rounded standout dark v-model="text" placeholder="Type something...">

        <template v-slot:append>
          <q-icon name="search" class="cursor-pointer" @click="searchProduct()" />
        </template>
      </q-input>

      <div class="q-pa-lg text-white">
        <q-option-group
          v-model="marketplace"
          :options="options"
          color="purple-14"
          type="toggle"
          inline
        ></q-option-group>
      </div>

    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const marketplace = ref(['Amazon'])
const text = ref('')

const options = [
  { label: 'Amazon', value: 'Amazon' },
  { label: 'eBay', value: 'eBay' },
  { label: 'Allegro', value: 'Allegro' },
  { label: 'Kaufland', value: 'Kaufland' },
  { label: 'Morele', value: 'Morele' },
  { label: 'RTV Euro AGD', value: 'RTV Euro AGD' },
  { label: 'MediaExpert', value: 'MediaExpert' },
]

async function searchProduct() {
  const response = await axios.get('http://127.0.0.1:8000/search', {
    params: {
      query: text.value,
      marketplaces: marketplace.value
    }
  })
  console.log(response)
}
</script>

<style scoped>
.q-input{
  margin-top: 1em;
  width: 100%;
}

</style>
