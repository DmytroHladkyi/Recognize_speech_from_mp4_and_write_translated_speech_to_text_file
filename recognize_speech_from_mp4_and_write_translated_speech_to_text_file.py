import speech_recognition as sr
from moviepy.video.io.VideoFileClip import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import deepl
from password import auth_key
import os

# Путь к видеофайлу и путь для сохранения аудио
video_path = r'path\to\file'

# Загружаем видео и извлекаем аудио дорожку
video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio

# Сохраняем аудио в формате WAV
wav_audio_path = r'path\to\folder\audio2.wav'
audio_clip.write_audiofile(wav_audio_path)

# Загрузка аудиофайла
audio_file = r'path\to\folder\audio2.wav'
sound = AudioSegment.from_mp3(audio_file)

# Преобразование аудиофайла в WAV
sound.export("temp.wav", format="wav")

# Инициализация объекта распознавания
recognizer = sr.Recognizer()

# Загрузка аудиофайла для распознавания
audio_data = sr.AudioFile("temp.wav")

# Попытка распознавания речи
with audio_data as source:
    audio = recognizer.record(source)

# Распознавание речи с использованием Google Web Speech API
try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print("Распознанный текст: ", text)
except sr.UnknownValueError:
    print("Не удалось распознать речь")
except sr.RequestError as e:
    print(f"Ошибка запроса к Google Web Speech API: {e}")

# Удаление временного WAV файла
os.remove("temp.wav")
os.remove(r'path\to\folder\audio2.wav') # если не хотим этот файл, чтобы он оставался

 # Replace with your key
translator = deepl.Translator(auth_key)

result = translator.translate_text(f"{text}", target_lang="EN-US")
print("Перевод на английский язык: ", result.text)
try:
    # Путь к папке для сохранения файла
    folder_path = "translator"

    # Проверка существования папки
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Запись переведенного текста в файл в указанной папке
    output_file_path = os.path.join(folder_path, "переведенный_текст.txt")
    with open(output_file_path, "w", encoding='utf-8') as text_file:
        text_file.write(result.text)
        
    # Запись распознанного текста в файл в указанной папке    
    output_file_path = os.path.join(folder_path, "распознанный_текст.txt")
    with open(output_file_path, "w", encoding='utf-8') as text_file:
        text_file.write(text)

except sr.UnknownValueError:
    print("Не удалось распознать речь")
