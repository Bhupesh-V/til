<template>
  <div class="post-metadata" v-if="createdDate">
    <div class="created-date">
      Posted on: {{ createdDate }}
    </div>
  </div>
</template>

<script setup>
import { useData } from 'vitepress'
import { computed } from 'vue'

const { frontmatter } = useData()

const formatDate = (date) => {
  if (!date) return null
  
  const dateObj = date instanceof Date ? date : new Date(date)
  
  if (isNaN(dateObj.getTime())) return null
  
  try {
    return dateObj.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  } catch (e) {
    console.warn('Error formatting date:', e)
    return null
  }
}

const createdDate = computed(() => {
  return frontmatter.value?.createdAtFormatted || 
         (frontmatter.value?.createdAt ? formatDate(frontmatter.value.createdAt) : null)
})
</script>

<style scoped>
.post-metadata {
  font-size: 0.9em;
  color: var(--vp-c-text-2);
  margin: 1em 0;
}

.created-date {
  white-space: nowrap;
}
</style>