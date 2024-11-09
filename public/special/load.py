from reactpy import component


@component
def Load():
  return """\n
    <script>
      window.onload = () => {
        const preloader = document.getElementById('preloader');
        preloader.style.display = 'none';
      } 
    </script>
    <style>
      #preloader{
        width: 100%;
        height: 100%;
      }
    </style>
    <div id="preloader">loading...</div> \n
  """
