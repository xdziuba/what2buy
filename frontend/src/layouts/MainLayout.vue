<template>
  <q-layout view="lHh Lpr lFf">

    <div id="vanta-bg"></div>

    <q-header elevated>
      <q-toolbar class="text-white">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title>What2Buy</q-toolbar-title>
        <div>v0.0.1</div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" bordered>
      <q-list>
        <q-item-label header>Menu</q-item-label>
        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import * as THREE from 'three'
import FOG from 'vanta/dist/vanta.fog.min'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'About',
    caption: 'What is What2Buy?',
    icon: 'school',
    link: '/about'
  },
  {
    title: 'Github',
    caption: 'Source Code Repository',
    icon: 'code',
    link: 'https://github.com/xdziuba/what2buy'
  }
]

const leftDrawerOpen = ref(false)
function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

let vantaEffect = null

onMounted(() => {
  vantaEffect = FOG({
    el: '#vanta-bg',
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.0,
    minWidth: 200.0,
    highlightColor: 0xff00f0,
    midtoneColor: 0x5a00ff,
    lowlightColor: 0x870293,
    baseColor: 0x1d0093,
    blurFactor: 0.9,
    speed: 1.7,
    zoom: 0.7,
    THREE
  })
})

onBeforeUnmount(() => {
  if (vantaEffect) vantaEffect.destroy()
})
</script>

<style scoped>
#vanta-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.q-layout,
.q-page-container {
  background: transparent !important;
}
.q-header {
  background: transparent;
}

.q-toolbar {
  background: #c000967c;
  background: linear-gradient(143deg, rgba(179, 0, 140, 0.479) 0%, rgba(123, 0, 255, 0.521) 87%, rgba(123, 0, 255, 0.479) 100%);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

</style>
