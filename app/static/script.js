{/* <script>
  $('.plus-cart').click(function () {
    var id = $(this).attr('pid').toString();
    var url = "{% url 'plus-cart' %}";  // Django template tag renders the correct URL here
    $.ajax({
      type: "GET",
      url: url,
      data: {
        prod_id: id
      },
      success: function (data) {
        console.log("Response:", data);
      },
      error: function (xhr, status, error) {
        console.log("Error:", error);
      }
    });
  });
</script> */}
