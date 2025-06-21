from time import time

# Function to count typing errors
def tperror(prompt, inprompt):
    prompt_words = prompt.split()
    input_words = inprompt.split()
    errors = 0
    for i in range(min(len(prompt_words), len(input_words))):
        if prompt_words[i] != input_words[i]:
            errors += 1
    # Count remaining extra or missing words as errors
    errors += abs(len(prompt_words) - len(input_words))
    return errors

# Function to calculate typing speed (words per minute)
def speed(inprompt, elapsed_time):
    words = inprompt.split()
    twords = len(words)
    wpm = (twords / elapsed_time) * 60
    return round(wpm, 2)

# Function to get elapsed time
def elapsedtime(stime, etime):
    return etime - stime

if __name__ == '__main__':
    prompt = "NumPy is the backbone of scientific computing in Python, enabling fast and efficient array operations used in data science, machine learning, and numerical computing."
    
    print("Type this:\n", prompt)
    input("\nPress Enter when you're ready to start typing...")
    
    # Start timing
    stime = time()
    inprompt = input("\nStart typing:\n")
    etime = time()
    
    # Calculations
    total_time = round(elapsedtime(stime, etime), 2)
    typing_speed = speed(inprompt, total_time)
    total_errors = tperror(prompt, inprompt)
    
    # Display results
    print("\n--- Typing Test Results ---")
    print("Total time elapsed:", total_time, "seconds")
    print("Your average typing speed:", typing_speed, "words per minute")
    print("Number of errors:", total_errors)

        