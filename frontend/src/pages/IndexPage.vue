<template>
  <q-page class="flex flex-center">
    <div class="search-content flex column flex-center">
      <div class="text-h2 text-white q-mb-lg">What are we searching today?</div>
      <q-input rounded standout dark v-model="text" placeholder="Type something...">

        <template v-slot:append>
          <q-icon name="search" class="cursor-pointer" @click="console.log('Searching for:', text)" />
        </template>
      </q-input>
    </div>
  </q-page>
</template>

<script setup>
//
</script>

<style scoped>
.q-input{
  margin-top: 1em;
  width: 100%;
}
</style>
