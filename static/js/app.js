function startLearning() {
    const topic = document.getElementById('topicInput').value.trim();
    
    if (!topic) {
        alert('Please enter a topic to learn about!');
        return;
    }
    
    // Show loading state
    const contentArea = document.getElementById('learningContent');
    contentArea.style.display = 'block';
    document.getElementById('contentTopic').textContent = 'Loading...';
    document.getElementById('contentDescription').textContent = 'Preparing your learning content...';
    document.getElementById('contentTips').innerHTML = '';
    
    // Make API call
    fetch('/api/learn', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: topic })
    })
    .then(response => response.json())
    .then(data => {
        // Update content
        document.getElementById('contentTopic').textContent = `Learning: ${data.topic}`;
        document.getElementById('contentDescription').textContent = data.content;
        
        // Create tips list
        const tipsList = document.createElement('ul');
        tipsList.className = 'tips-list';
        
        data.tips.forEach(tip => {
            const listItem = document.createElement('li');
            listItem.textContent = tip;
            tipsList.appendChild(listItem);
        });
        
        const tipsContainer = document.getElementById('contentTips');
        tipsContainer.innerHTML = '<h4>Learning Tips:</h4>';
        tipsContainer.appendChild(tipsList);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('contentDescription').textContent = 'Sorry, there was an error loading the content. Please try again.';
    });
}

// Allow Enter key to trigger learning
document.getElementById('topicInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        startLearning();
    }
});