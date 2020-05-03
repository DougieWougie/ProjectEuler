Module Module1

  Sub Main()
    Dim beganAt As Date = Now
    Dim n As Integer = 2000000
    Dim total As Long = 0

    For counter As Integer = 2 To n
      If isPrime(counter) = True Then
        total = total + counter
      End If
    Next

    Dim endAt As Global.System.TimeSpan = Now.Subtract(beganAt)
    Dim took As Integer = endAt.Milliseconds

    Console.WriteLine(total.ToString + " in " + took.ToString + " ms.")
    Console.ReadKey()
  End Sub

  Private Function isPrime(ByVal thisNumber As Integer) As Boolean
    ' Prime numbers other than two are odd...
    If thisNumber = 2 Then
      Return True
    ElseIf thisNumber Mod 2 = 0 Then
      Return False
    End If

    'Check it isn't divisible by up to its square root
    '(consider n=(root n)(root n) as factors)
    For counter As Integer = 3 To (Math.Sqrt(thisNumber)) Step 2
      If thisNumber Mod counter = 0 Then
        Return False
      End If
    Next
    Return True
  End Function

End Module
