<template>
  <a :href="link" class="VPLink highlighted-link" target="_blank" rel="noreferrer">
    <span>
    {{ text }}
    </span>
  </a>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    required: true,
  },
  link: {
    type: String,
    required: true,
  },
});
</script>

<style scoped>
.highlighted-link {
  color: var(--vp-c-brand); /* Default link color */
  display: flex;
    align-items: center;
    font-size: 14px;
    padding-right: 12px;
    font-weight: 500;
    color: var(--vp-c-text-1);
    transition: color 0.25s;
}

span {
    padding: 3px 8px;
    color: white;
    border-radius: .375rem;
    background: #378f2d;
}

span:hover {
  transform: translate(0, 0) rotate(0) skewX(0) skewY(0) scaleX(1.05) scaleY(1.05);
}


.dark .highlighted-link {
  color:rgb(255, 255, 255); /* Custom color for dark mode */
}
</style>