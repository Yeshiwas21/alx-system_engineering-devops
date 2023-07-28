#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_loop - creates an infinite loop to make the program hang
 * Return: always 0
 */
int infinite_loop(void)
{
    while (1)
    {
        sleep(1);
    }
    return 0;
}

/**
 * main - creates 5 child processes
 * Return: always 0
 */
int main(void)
{
    int num_children = 5;
    pid_t child_pid;

    for (int i = 0; i < num_children; i++)
    {
        child_pid = fork();
        if (child_pid == 0)
            return 0;

        printf("Child process created, PID: %d\n", child_pid);
    }

    infinite_loop();
    return 0;
}

