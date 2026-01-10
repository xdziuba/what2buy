import { defineStore } from 'pinia'
import type { SearchResult } from 'src/types/SearchResult'

export const useSearchStore = defineStore('search', {
  state: () => ({
    result: null as SearchResult | null
  }),

  actions: {
    setResult(result: SearchResult) {
      this.result = result
    },

    clear() {
      this.result = null
    }
  }
})