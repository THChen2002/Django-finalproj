for (var i = 0; i < notifications.length; i++) {
  //alert(notifications[i]);
  var notification = notifications[i];
  var dateStr = notification.fields.timestamp;
  var date = new Date(dateStr);
  var year = date.getFullYear();
  var month = ('0' + (date.getMonth() + 1)).slice(-2);
  var day = ('0' + date.getDate()).slice(-2);
  var hour = ('0' + date.getHours()).slice(-2);
  var minute = ('0' + date.getMinutes()).slice(-2);
  var formattedDate = year + '-' + month + '-' + day + ' ' + hour + ':' + minute;
  document.write("<li>");
  document.write(`<a class='dropdown-item' href='#' onclick='markNotificationRead(${notification.pk})' style='position: relative; align-items: center; width: 100%;'>`);
  document.write(`<span class="position-absolute top-50 start-5 translate-middle border border-light rounded-circle" id='notification-${notification.pk}' style="width: 15px; height: 15px; background-color: #ff2433;"> `);
  document.write(`</span>`);
  document.write("<p style='padding-left:20px';>" + notification.pk + "</p>");
  document.write("<h5 style='padding-left:20px';>" + notification.fields.verb + "</h5>");
  document.write("<p style='padding-left:20px';>" + notification.fields.description + "</p>");
  document.write("<p style='padding-left:20px';>" + formattedDate + "</p>");
  document.write("<hr style='margin-top:0px; margin-bottom: 0px;'>");
  document.write("</a>");
  document.write("</li>");
  function markNotificationRead(pk) {
    if (pk == 0) {
        var notificationItems = document.querySelectorAll('[id^="notification"]');
        notificationItems.forEach(item => {
          //item.style.backgroundColor = 'transparent';
          item.style.display = 'none';
        });
    }else {
        var notificationItem = document.getElementById(`notification-${pk}`);
        //notificationItem.style.backgroundColor = 'transparent';
        notificationItem.style.display = 'none';
    }
    //alert("notification-" + pk);
    var dataToSend = {'id': pk};
    var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    fetch(viewUrl, {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken},
        body: JSON.stringify(dataToSend)
    })
    .then(response => {
        console.log(response);
    })
    .catch(error => {
        console.error(error);
        // 處理錯誤
    });
  }
}