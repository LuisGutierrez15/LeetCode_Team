function shortestPalindrome(s: string): string {
    if(s.trim().length === 0 || s == '' || s.length == 1) return s
    let s_mirror: string = s.split('').reverse().join('');

    let step: number = 0

    while(true){
        let test:  string = s
        let temp: string = s_mirror.slice(0, step)
        test = [temp,test].join('')

        let is_odd: boolean = test.length % 2 == 1
        let plus: number = is_odd ? 1 : 0

        let leftHalf: string = test.slice(0, Math.floor(test.length / 2) + plus).split('').reverse().join('')
        let rightHalf: string = test.slice(Math.floor(test.length / 2), test.length)
        
        if(leftHalf == rightHalf){
            return test
        }
        
        step += 1
    }
};