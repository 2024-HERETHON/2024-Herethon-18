document.getElementById('settingToggleContainer').addEventListener('click', function () {
    let settingToggleContainer = this;
    let toggleButton = settingToggleContainer.querySelector('.setting-toggle-btn');
    if (settingToggleContainer.classList.contains('on')) {
        settingToggleContainer.classList.remove('on');
        toggleButton.textContent = '비동의';
        toggleButton.style.left = 'calc(100% - 87.4px + 2px)';
    } else {
        settingToggleContainer.classList.add('on');
        toggleButton.textContent = '동의';
        toggleButton.style.left = '-2px';
    }
});


// 비밀번호 동일한지 확인
document.addEventListener('DOMContentLoaded', () => {
    const accountDeleteBtn = document.getElementById('accout-delete-btn');
    const modal = document.getElementById('password-alert');
    const closeModalBtn = document.getElementById('password-alert-btn');

    accountDeleteBtn.addEventListener('click', () => {
        modal.style.display = 'block';
    });

    closeModalBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    const newPasswordInput = document.getElementById('new-password');
    const confirmPasswordInput = document.getElementById('confirm-password');
    const correctMessage = document.querySelector('.correct-message');
    const errorMessage = document.querySelector('.error-message');

    confirmPasswordInput.addEventListener('input', () => {
        if (newPasswordInput.value === confirmPasswordInput.value) {
            correctMessage.style.display = 'block';
            errorMessage.style.display = 'none';
        } else {
            correctMessage.style.display = 'none';
            errorMessage.style.display = 'block';
        }
    });
});

// 모달
document.getElementById('accout-delete-btn').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('password-alert').style.display = 'block';
});

document.getElementById('password-alert-btn').addEventListener('click', function() {
    document.getElementById('password-alert').style.display = 'none';
});
