import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        joke_data = response.json()
        return joke_data
    except requests.RequestException as e:
        print(f"Помилка при отриманні анекдота: {e}")
        return None

def main():
    joke = get_joke()
    if not joke:
        return
    
    print("\nАнекдот:")
    print(joke['setup'])
    print(joke['punchline'])

if __name__ == "__main__":
    main()
