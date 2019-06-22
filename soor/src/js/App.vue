<template>
  <div>
    <div class="main">
        <chat> </chat>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
import chat from '@/components/Chat'

export default {
  name: 'App',  
  components: {
    chat,
  }
}
</script>

<style>
.main{
  width: 100%;
}
</style>
