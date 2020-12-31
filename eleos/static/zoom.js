function delete_meeting(meeting_id){

    const csrftoken = document.querySelector("input[name=csrfmiddlewaretoken]").value;

    const request = new Request(
        document.location.href,
        {headers: {'X-CSRFToken': csrftoken, 'Content-Type': 'application/x-www-form-urlencoded'}}
    );

    fetch(request, {
        method: 'POST',
        body: `meeting_id=${meeting_id}`,
    })
    .then(response => response.json())
    .then(data => {
        if (data==204){
            let container = document.querySelector(`#m${meeting_id}`);
            container.remove();
        }
    });
}